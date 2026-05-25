---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Artifact]]", "[[Deadly d8]]", "[[Disarm]]", "[[Divine]]", "[[Finesse]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The origins of this *+3 greater striking rapier* are shrouded in mystery, but it earned its name in the hands of an unknown hero who used it to singlehandedly defend a remote Nirmathi village from a vicious gang of bandits, shrugging off dozens of blows that would have felled any other mortal. Only when all of the bandits had been dispatched or driven off did the noble warrior finally succumb to their injuries.

While wielding *Final Stand*, if you take damage that would reduce you to 0 Hit Points but not immediately kill you, attempt a DC 11 flat check. If you succeed, you avoid being knocked out and remain at 1 Hit Point instead. For the remainder of the encounter, you can't regain Hit Points in any way, though you can be stabilized if you gain the dying condition. If you're still conscious and there are no nearby enemies that you can perceive, you immediately drop to 0 Hit Points and are dying 1. If you have any other abilities that would allow you to remain at 1 Hit Point when you would be reduced to 0 Hit Points (such as [[Orc Ferocity]]), you must use those abilities before you can benefit from Final Stand's ability.

**Destruction** If the wielder of *Final Stand* surrenders to their enemies while any of their allies are still standing, the blade weakens and the DC of the flat check permanently increases by 2. Final Stand shatters into hundreds of pieces the moment the DC of the flat check is ever higher than 20.

**Source:** `= this.source` (`= this.source-type`)
