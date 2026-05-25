---
type: item
source-type: "Remaster"
level: "23"
traits: ["[[Agile]]", "[[Artifact]]", "[[Concealable]]", "[[Concussive]]", "[[Fatal d10]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

One dueling pistol in this paired set is etched with flames along its barrel, while the other is etched with icicles. In these separate forms, one gun comprising the *Coldstar Pistols* functions as a *+3 greater striking greater flaming dueling pistol* and the other as a *+3 greater striking greater frost dueling pistol*. When joined, the guns form a double-barreled weapon that functions as a *+4 major striking greater flaming greater frost dueling pistol*. The combined form has a range increment of 120 feet. In either form, the *Coldstar Pistols* have the agile, concealable, concussive, and fatal d10 traits. As star guns, the *Coldstar Pistols* run on magic and don't use ammunition or black powder.

**Activate** `pf2:1` (manipulate)

**Effect** You switch the Coldstar Pistols from one form to the other. Attempt a Deception check to [[Feint]] with a +4 circumstance bonus.

**Activate** `pf2:1` (manipulate)

**Frequency** once per round

**Effect** Make two Strikes against one target, taking the highest of the two attack rolls and applying it to both attacks. Your multiple attack penalty increases only after these Strikes.

**Destruction** If Deft Onki's name and deeds ever fade from mortal memory entirely, the Coldstar Pistols can be destroyed like a normal object.

**Source:** `= this.source` (`= this.source-type`)
