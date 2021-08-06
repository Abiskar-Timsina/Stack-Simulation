import pygame as pygame


def main():
    screen =pygame.display.set_mode((1500, 820))
    font =pygame.font.Font(None, 32)
    clock =pygame.time.Clock()
    input_box =pygame.Rect(10, 50, 140, 32)
    color_inactive =pygame.Color('lightskyblue3')
    color_active =pygame.Color('dodgerblue2')
    text_color=pygame.Color('white')
    terminal_text_color=pygame.Color('grey')
    push_button_color=pygame.Color('#07A965')
    pop_button_color=pygame.Color('#C20C0C')
    color = color_inactive
    active = False
    max_stack_size=0
    text = ''
    message = ''
    terminal_cursor_pos = 0
    done = False

    while not done:
        
        if max_stack_size == 0:
            prompt_txt='Enter the size of the stack:'
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    done = True
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type ==pygame.KEYDOWN:
                    if active:
                        if event.key ==pygame.K_RETURN:
                            max_stack_size=int(text)
                            message='stack size: ' + text
                            print('stack size',max_stack_size)
    
                            text=''

                        elif event.key ==pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((30, 30, 30))
            # Render the current text.
            prompt1 = font.render(prompt_txt,True,text_color)
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(prompt1,(10,10))
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)
        else:
            prompt_txt='Enter element to push into the stack:'
            prompt_txt2='Pop from the stack:'
            push_button =pygame.Rect(input_box.w+20,50,70,32)
            pop_button =pygame.Rect(input_box.centerx+5,input_box.bottom+80,70,32)
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    done = True
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive

                    #For push button click.
                    if push_button.collidepoint(event.pos):
                        element=int(text)
                        message = text + ' is pushed into the stack'
                        print('element',element)
                        text=''
                    #For pop button click.
                    if pop_button.collidepoint(event.pos):
                        print("pop operation")
                        message = 'pop operation'
                if event.type ==pygame.KEYDOWN:
                    if active:
                        if event.key ==pygame.K_RETURN:
                            element=int(text)
                            message = text + ' is pushed into the stack'
                            print('element',element)
                            text=''

                        elif event.key ==pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((30, 30, 30))
            # Render the current text.
            prompt1 = font.render(prompt_txt,True,text_color)
            prompt2 = font.render(prompt_txt2,True,text_color)
            txt_surface = font.render(text, True, color)
            push_button_text=font.render('PUSH', True,push_button_color)
            pop_button_text=font.render('POP', True,pop_button_color)
            # Resize the box if the text is too long.
            width = max(150, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(prompt1,(10,10))
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            screen.blit(push_button_text, (push_button.centerx-(push_button_text.get_width()/2), push_button.centery-(push_button_text.get_height())/2))
            screen.blit(prompt2,(10,input_box.bottom+50))
            screen.blit(pop_button_text, (pop_button.centerx-(pop_button_text.get_width()/2), pop_button.centery-(pop_button_text.get_height())/2))

            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)
            #Blit the push button
            pygame.draw.rect(screen, push_button_color, push_button, 2)
            #Blit the pop button
            pygame.draw.rect(screen, pop_button_color, pop_button, 2)

        # Blit Vertical line,
        pygame.draw.aaline(screen, text_color, (prompt1.get_width()+30, 0), (prompt1.get_width()+30, 820),1)

        # Blit Horizontal line,
        pygame.draw.aaline(screen, text_color, (0, 500), (prompt1.get_width()+30, 500),1)


        # Display Terminal text.
        terminal_message = font.render(message, True, terminal_text_color)
        screen.blit(terminal_message,(10,530+terminal_cursor_pos))
        
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()