---
type: location
sub-type: Castle
location: "[[Example Parent Location]]"
faction: "[[Example Faction]]"
---
### `= this.file.name`
**`= this.sub-type`** `= choice(this.location != null, "(" + this.location + ")", "")`
`= choice(this.faction != null, "**Faction** " + this.faction, "")`

Somewhere inside example [[Example Parent Location]].

#### Locations
``` dataview
LIST sub-type
WHERE location = this.file.link AND lower(type) = "location"
```

#### Factions
``` dataview
LIST
WHERE hq = this.file.link AND lower(type) = "faction"
```

#### Characters
``` dataview
LIST WITHOUT ID file.link + choice(title != null OR faction != null, " (" + choice(title != null, title, "") + choice(title != null AND faction != null, ", ", "") + choice(faction != null, faction, "") + ")", "")
WHERE location = this.file.link AND (lower(type) = "npc" OR lower(type) = "pc")
```

#### Encounters
``` encounter-table

name: {encounter.name}
party: {party}
creatures:
  1: {creature/npc}
```
