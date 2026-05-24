---
type: faction
sub-type: "{sub-type}"
goal: "{goal}"
leader: "{wikilink:npc}"
hq: "{wikilink:location}"
scope: "{scope}"
scope-location: "{wikilink:location}"
structure: "{structure}"
---
### `= this.file.name`
**`= this.sub-type`** `= choice(this.scope != null, this.scope + choice(this.scope-location != null, " (" + this.scope-location + ")", ""), "")`
**Leader** `= this.leader`
**Goal** `= this.goal`
**Structure** `= this.structure`

{description}

##### Organisation
{organisation}

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