import { Component } from '@angular/core';

@Component({
  selector: 'app-values',
  standalone: true,
  imports: [],
  templateUrl: './values.component.html',
  styleUrl: './values.component.css'
})
export class ValuesComponent {
  // example of dynamic content
  values = [
    {
      title: 'Объединение учеников и выпускников',
      description: 'Мы стремимся создать платформу для обмена опытом и поддержания связи.'
    },
    {
      title: 'Открытость и доброжелательность',
      description: 'Мы призываем всех пользователей быть открытыми и готовыми помочь друг другу.'
    },
    {
      title: 'Развитие и рост',
      description: 'Мы поддерживаем постоянное развитие наших пользователей независимо от времени и расстояний.'
    }
  ];
}
