import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraImovelComponent } from './altera-imovel.component';

describe('AlteraImovelComponent', () => {
  let component: AlteraImovelComponent;
  let fixture: ComponentFixture<AlteraImovelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlteraImovelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlteraImovelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
