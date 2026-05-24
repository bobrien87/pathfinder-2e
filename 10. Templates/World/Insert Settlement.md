---
type: settlement
sub-type: "{sub-type}"
level: "{level}"
alignment: "{alignment}"
location: "{[[location]]}"
population: "{population}"
demographics: "{demographics}"
government: "{government}"
ruler: "{ruler}"
languages: "{languages}"
religions: "{religions}"
source: "{source}"
source-type: "{source-type}"
---
### `= this.file.name`
**`= choice(this.level != null, "Level " + this.level + " ", "") + choice(this.sub-type != null, this.sub-type, "Settlement")`**`= choice(this.alignment != null, "; **" + this.alignment + "**", "")`
`= choice(this.location != null, "**Location** " + this.location, "") + choice(this.government != null, choice(this.location != null, "; ", "") + "**Government** " + this.government, "") + choice(this.ruler != null, choice(this.location != null or this.government != null, "; ", "") + "**Ruler** " + this.ruler, "") + choice(this.population != null, choice(this.location != null or this.government != null or this.ruler != null, "<br>", "") + "**Population** " + this.population + choice(this.demographics != null, " (" + this.demographics + ")", ""), "") + choice(this.languages != null or this.religions != null, choice(this.location != null or this.government != null or this.ruler != null or this.population != null, "<br>", "") + choice(this.languages != null, "**Languages** " + this.languages, "") + choice(this.religions != null, choice(this.languages != null, "; ", "") + "**Religions** " + this.religions, ""), "")`

***

{description}

#### Points of Interest
{points-of-interest}

#### Active Factions
``` dataview
LIST
WHERE hq = this.file.link OR contains(scope-location, this.file.link) AND type = "faction"
```

#### Characters
``` dataview
LIST title
WHERE location = this.file.link AND (type = "npc" OR type = "pc")
```

**Source:** `= this.source` `= choice(this.source-type != null, "(" + this.source-type + ")", "")`
