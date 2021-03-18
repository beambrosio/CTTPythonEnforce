import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraClienteComponent } from './altera-cliente.component';

describe('AlteraClienteComponent', () => {
  let component: AlteraClienteComponent;
  let fixture: ComponentFixture<AlteraClienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlteraClienteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlteraClienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
