import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraCompraComponent } from './altera-compra.component';

describe('AlteraCompraComponent', () => {
  let component: AlteraCompraComponent;
  let fixture: ComponentFixture<AlteraCompraComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlteraCompraComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlteraCompraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
