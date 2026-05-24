---
type: Faction
sub-type: Military Unit
goal: Defend the Kingdom
leader: "[[Example NPC]]"
hq: "[[Example Location]]"
scope: Regional
scope-location: "[[Example Location]]"
structure: Military chain of command
---
### `= this.file.name`
**`= this.sub-type`** `= choice(this.scope != null, this.scope + choice(this.scope-location != null, " (" + this.scope-location + ")", ""), "")`
**Leader** `= this.leader`
**Goal** `= this.goal`
**Structure** `= this.structure`

The elite guard of Example Location.

##### Organisation
- Lord Commander (commanding the unit)
	- Two Captains (each commanding a detachment)
		- Four Sergeants (each commanding a squad)

#### Members
``` dataview
LIST title
WHERE contains(faction, this.file.link) AND (lower(type) = "pc" OR lower(type) = "npc")
```

#### Encounters
``` encounter-table

name: {encounter.name}
party: {party}
creatures:
  1: {creature/npc}
```