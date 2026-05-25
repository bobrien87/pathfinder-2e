---
type: faction
faction: "{[[faction]]}"
sub-type: "{sub-type}"
goal: "{goal}"
leader: "{wikilink:npc}"
hq: "{wikilink:location}"
scope: "{scope}"
scope-location: "{wikilink:location}"
structure: "{structure}"
---
### `= this.file.name`
**`= this.sub-type`** `= choice(this.scope != null and this.scope != "", this.scope + choice(this.scope-location != null and this.scope-location != "", " (" + this.scope-location + ")", ""), "")`
**Leader** `= this.leader`
**Goal** `= this.goal`
**Structure** `= this.structure`
`= choice(this.faction != null and this.faction != "", "**Parent Faction** " + this.faction, "")`

{description}

##### Organisation
{organisation}

##### Sub-factions
``` dataview
LIST
WHERE contains(faction, this.file.link) AND lower(type) = "faction"
```

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