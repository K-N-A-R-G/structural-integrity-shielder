

# --- SYNC DATA BLOCK: COLLECTIONS ---
            for k in vars(OrderedDict()):
                state.pop(k, None)
                slots.pop(k, None)
            if slots:
                state = state, slots
            else:
                state = state or None
        return self.__class__, (), state, None, iter(self.items())

    def copy(self):
        'od.copy() -> a shallow copy of od'

# --- END OF NODE UPDATE ---
