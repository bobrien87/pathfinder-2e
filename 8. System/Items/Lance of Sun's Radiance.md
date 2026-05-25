---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Deadly d8]]", "[[Jousting d6]]", "[[Light]]", "[[Magical]]", "[[Reach]]"]
price: "{'gp': 1450}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted for a long-forgotten knight to slay Avathrael Realmshaper, this *+2 striking dragon bane lance* is crafted from gleaming steel with a golden silk banner depicting a radiant sun. When in a location of dim light or darkness, the *lance of sun's radiance* sheds bright light in a 60-foot radius, and dim light for a further 60 feet.

**Activate—Banish Darkness** `pf2:1` (divine, light, manipulate)

**Frequency** once per hour

**Effect** You tap the lance's tip against an object, causing that object to shed light like a torch for 1 hour.

**Activate—Sun Cutting Scales** `pf2:2` (divine, light, manipulate)

**Frequency** once per day

**Effect** With a bold proclamation, you thrust the lance forward, firing a beam of brilliant, scouring light in a @Template[line|distance:120]. Creatures in the area take 6d8 spirit damage, or 6d12 spirit damage if they're a dragon (DC 28 [[Reflex]] save). Creatures that critically fail are also [[Blinded]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
