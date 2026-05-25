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
**`= choice(this.level != null and this.level != "", "Level " + this.level + " ", "") + choice(this.sub-type != null and this.sub-type != "", this.sub-type, "Settlement")`**`= choice(this.alignment != null and this.alignment != "", "; **" + this.alignment + "**", "")`
`= choice(this.location != null and this.location != "", "**Location** " + this.location, "") + choice(this.government != null and this.government != "", choice(this.location != null and this.location != "", "; ", "") + "**Government** " + this.government, "") + choice(this.ruler != null and this.ruler != "", choice(this.location != null and this.location != "" or this.government != null and this.government != "", "; ", "") + "**Ruler** " + this.ruler, "") + choice(this.population != null and this.population != "", choice(this.location != null and this.location != "" or this.government != null and this.government != "" or this.ruler != null and this.ruler != "", "<br>", "") + "**Population** " + this.population + choice(this.demographics != null and this.demographics != "", " (" + this.demographics + ")", ""), "") + choice(this.languages != null and this.languages != "" or this.religions != null and this.religions != "", choice(this.location != null and this.location != "" or this.government != null and this.government != "" or this.ruler != null and this.ruler != "" or this.population != null and this.population != "", "<br>", "") + choice(this.languages != null and this.languages != "", "**Languages** " + this.languages, "") + choice(this.religions != null and this.religions != "", choice(this.languages != null and this.languages != "", "; ", "") + "**Religions** " + this.religions, ""), "")`

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

**Source:** `= this.source` `= choice(this.source-type != null and this.source-type != "", "(" + this.source-type + ")", "")`
