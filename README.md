# onyx_taxi

Начальная стадия реализации сервиса заказа такси.

Краткое описание:
Централизованный сервис для хранения данных о заказах такси.

Пользователи сервиса — мобильные приложения пассажира и водителя.

Клиентов можно создавать, искать, удалять. Изменять данные клиента нельзя, лучше удалить и создать нового.

Данные водителей тоже только создавать, искать и удалять. Вместо изменения также удалить и создать нового.

Заказы только создаются, ищутся и изменяются.

Удалить заказ не должно быть позволено. В случае если заказ отменён — поставить в колонку статус о том что он отменён.

Последовательности смены статусов заказа допускаются только такие:

not_accepted → in_progress → done;

not_accepted → in_progress → cancelled;

not_accepted → cancelled.

Менять дату создания, id водителя и id клиента можно только в случае если статус заказа - not_accepted.
