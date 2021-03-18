import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraGastosComponent } from './altera-gastos.component';

describe('AlteraGastosComponent', () => {
  let component: AlteraGastosComponent;
  let fixture: ComponentFixture<AlteraGastosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlteraGastosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlteraGastosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
