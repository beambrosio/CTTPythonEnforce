import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlteraProprietarioComponent } from './altera-proprietario.component';

describe('AlteraProprietarioComponent', () => {
  let component: AlteraProprietarioComponent;
  let fixture: ComponentFixture<AlteraProprietarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlteraProprietarioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlteraProprietarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
