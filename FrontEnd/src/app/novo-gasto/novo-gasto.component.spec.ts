import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovoGastoComponent } from './novo-gasto.component';

describe('NovoGastoComponent', () => {
  let component: NovoGastoComponent;
  let fixture: ComponentFixture<NovoGastoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NovoGastoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NovoGastoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
