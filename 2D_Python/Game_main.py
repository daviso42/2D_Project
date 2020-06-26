#import os
#os.environ["SDL_VIDEODRIVER"] = "dummy"
from Class_and_Function import *

clock = pg.time.Clock() 

run = True
pg.mixer.music.play(-1)
facing = 1
moving = 1
spawn_count = 0
#backgroundlst.append(back)
while(run):
      clock.tick(70)
      
############################################################################################################
#
#     Check for initial events
#
############################################################################################################

      for event in pg.event.get():
            if event.type == pg.QUIT:
                  run = False
            if event.type == pg.MOUSEBUTTONDOWN: #checks for firing
                  shoot_sound.play()
                  guy.fire = True
            #if event.type == pg. MOUSEBUTTONUP:
            else:
                  guy.fire = False

############################################################################################################
#
#     Checking for Movement inputs
#
############################################################################################################

      #guy.standing = True
      #guy.left = False
      #guy.right = False
      keys = pg.key.get_pressed()
      if keys[pg.K_LSHIFT] and not guy.isDuck: #Sprint
            guy.fire = False
            guy.sprint = True
      else:
            guy.sprint = False
                        
      if keys[pg.K_a] and not keys[pg.K_d]: ## Wlak Left
            guy.standing = False
            guy.right = False
            guy.left = True
            guy.facing = -1
            moving = -1
            facing = -1
            if guy.x > 0:
                  for bkg in backgroundlst:
                        if guy.sprint:
                              bkg.x += bkg.svel
                        if guy.isDuck:
                              bkg.x += bkg.dvel
                        else:
                              bkg.x +=  bkg.vel

                       
      elif keys[pg.K_d]:# and not keys[pg.K_a]: # Walk Right
            guy.standing = False
            guy.left = False
            guy.right = True
            guy.facing = 1
            facing = 1
            if guy.x < set_width - guy.width:
                  for bkg in backgroundlst:
                        if guy.sprint:
                              bkg.x -= bkg.svel
                        if guy.isDuck:
                              bkg.x -= bkg.dvel
                        else:
                              bkg.x -=  bkg.vel
      else:
            guy.standing = True
                     
      if not keys[pg.K_s] and guy.height < 64: # Duck
            guy.isDuck = False
            guy.height += 2
            guy.y-=2
                              
############################################################################################################
#
#     Updating bullet list
#
############################################################################################################
      for bullet in bullets:
            for hit_index, badguy in enumerate(bad_guys):
                  hit = check_hitbox(bullet.hitbox, badguy.hitbox, facing, bullets, bullets.index(bullet))
                  if hit == True:
                        bullet.skip = True
                        badguy.health -= 1
                        if badguy.health < 1:
                              bad_guys.pop(hit_index)
                        break
            if bullet.skip:
                  bullet.skip = False
                  continue
            elif bullet.x <set_width and bullet.x >0:
                  bullet.x += bullet.vel
            else:
                  bullets.pop(bullets.index(bullet)) # remove bullet from the screen at border

############################################################################################################
#
#     Updating slug list
#
############################################################################################################
      for slug in slugs:
            slug.slugDelay += 1
            for hit_index, badguy in enumerate(bad_guys):
                  if slug.facing == 1:
                        hit = check_hitbox(slug.hitbox, badguy.hitbox, 1, slugs, slugs.index(slug))
                        if hit == True:
                              guy.eatSlugs = False
                              bad_guys.pop(hit_index)
                              continue
                  if slug.facing == -1:
                        hit = check_hitbox(slug.hitbox, badguy.hitbox, -1, slugs, slugs.index(slug))
                        if hit == True:
                              guy.eatSlugs = False
                              bad_guys.pop(hit_index)
                              continue
            if slug.slugDelay >=30:
                  guy.eatSlugs = False
            if slug.slugCount >= -30:
                  sneg = 1
                  if slug.slugCount < 0:
                        sneg = -1
                  if slug.y < ground:
                        slug.y -= round((slug.slugCount ** 2- (27*slug.slugCount)) * 0.2 * sneg)
                        if slug.y + 20 > ground:
                              slug.y = ground - 20
                        if slug.x >= 0 and slug.x + 35 <= set_width and slug.y != ground - 20:
                              slug.x += round(slug.vel *1.3)
                        else:
                              if keys[pg.K_d]:
                                    if guy.sprint:
                                          slug.x -= back.svel
                                    elif guy.isDuck:
                                          slug.x -= back.dvel
                                    else:
                                          slug.x -= back.vel
                              elif keys[pg.K_a]:
                                    if guy.sprint:
                                          slug.x += back.svel
                                    elif guy.isDuck:
                                          slug.x += back.dvel
                                    else:
                                          slug.x += back.vel


                  slug.slugCount -= .5
                  
            

            else:
                  slugs.pop(slugs.index(slug))
                  guy.eatSlugs = False


            

      

############################################################################################################
#
#     Checking for jumps
#
############################################################################################################

      if not(guy.isJump) and not(guy.isSJump):
            if (keys[pg.K_SPACE] and keys[pg.K_LSHIFT]) and not(guy.isDuck):
                  sjump_sound.play()
                  guy.isSJump = True
                  guy.jumpCount = 9
            elif keys[pg.K_SPACE]:
                  njump_sound.play()
                  guy.isJump = True
                  guy.jumpCount = 10

      else:
            if (guy.jumpCount >= -10 and guy.isJump) or (guy.jumpCount >= -9 and guy.isSJump):
                  neg = 1
                  if (guy.jumpCount < 0 and guy.isJump) or (guy.jumpCount < 0 and guy.isSJump):
                        neg = -1
                  if guy.isSJump:
                        guy.y -= round((guy.jumpCount ** 2) * 0.6 * neg) 
                        guy.jumpCount -= .5
                  else:
                        guy.y -= round((guy.jumpCount ** 2 ) * 0.17 * neg)
                        guy.jumpCount -= .5
            else:
                  guy.isJump = False
                  guy.isSJump = False
                  
############################################################################################################
#
#      Checking for duck inputs
#
############################################################################################################

      if not(guy.isDuck):
            if keys[pg.K_s] and not(guy.isJump) and not(guy.isSJump):
                  guy.isDuck = True

                  
      if(guy.isDuck):
            if guy.height >=40:
                  guy.height -=2
                  guy.y +=2
############################################################################################################
#
#     Selecting fire method
#
############################################################################################################

      if guy.fire:
            if guy.right:
                  facing = 1 #dictates shooting direction
            else:
                  facing = -1
            if len(bullets) < 10:
                  bullets.append(proj(round(guy.x + guy.width//2), round(guy.y + guy.height//4),38, 20, GREEN, guy.facing))
                  guy.fire = False

      if not guy.eatSlugs:
            if keys[pg.K_e] and not keys[pg.K_LSHIFT]:

                  guy.eatSlugs = True
                  if guy.right:
                        facing =1
                  else:
                        facing = -1
                  if len(slugs) < 2 :
                        slug =proj(round(guy.x + guy.width/2),round(guy.y),33, 20,RED, facing)
                        slugs.append(slug)

############################################################################################################
#
# Moving the Background
#
############################################################################################################
                        


      if guy.right:
            for num, bkg in enumerate(backgroundlst):
                  if bkg.x + bkg.width <= 0:
                        backgroundlst.pop(backgroundlst.index(bkg))
            if (backgroundlst[-1].x + set_width < set_width) and (len(backgroundlst) < 3):
                        backgroundlst.append(background(sbackground, set_width, bkg.y, set_width, set_height, 1))


      else:
            for num, bkg in enumerate(backgroundlst):
                  if bkg.x  >= set_width:
                        backgroundlst.pop(backgroundlst.index(bkg))

            if backgroundlst[0].x > 0 and len(backgroundlst) <3:
                  backgroundlst.append(background(sbackground, backgroundlst[0].x-set_width, bkg.y, set_width, set_height, -1))


############################################################################################################
#
# Check speed for enemy movement
#
############################################################################################################

      

############################################################################################################
#
# Enemy List
#
############################################################################################################





      
      for badguy in bad_guys:
            speed = check_speed(guy.standing, guy.sprint, guy.isDuck, moving, badguy.moving)
            badguy.move(moving,set_width, guy.standing, speed)

            
      if len(bad_guys) < 8:
            if spawn_count > 200:
                  bad_guys.append(bad(900, random.randint(ground - 100, ground - 60), 64, 64, False))
                  spawn_count = 0


                        

      spawn_count += 1
      
############################################################################################################
#
# Set up the next frame
#
############################################################################################################
      
      #enemy.move(moving, set_width, guy.standing, speed)
      moving = 1
      redraw(window)

pg.quit()
      
