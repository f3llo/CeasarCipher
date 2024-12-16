#include "SDL2/SDL.h"   /* All SDL App's need this */
#include <stdbool.h>
#include <stdio.h>

int main() {

	SDL_Init(SDL_INIT_VIDEO);
	bool quit = false;
	SDL_Event event;

	SDL_Window *window = SDL_CreateWindow("Pong", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
	SDL_Renderer *render = SDL_CreateRenderer(window, -1, 0);

	SDL_Rect rect = { .x = 200, .y = 200, .w = 30, .h = 30};

	SDL_SetRenderDrawColor(render, 255, 255, 255, 255);
	SDL_RenderFillRect(render, &rect);

	while(!quit){
		SDL_WaitEvent(&event);

		switch(event.type){
			case SDL_QUIT:
				quit = true;
				break;
			case SDLK_UP:
				rect.y += 1;
		}
		SDL_RenderPresent(render);
		SDL_RenderClear(render);
	}

	SDL_DestroyWindow(window);
	SDL_DestroyRenderer(render);
	SDL_Quit();
	return(0);
}
