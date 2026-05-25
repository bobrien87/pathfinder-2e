---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Earth]]", "[[Magical]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Jabali's dice* are two six-sided dice carved from evenly weighted stone to the specifications of a specific jabali shuyookh. The sides showing a 6 also have the name and title of the shuyookh inscribed in Petran. If you whisper the name and title during a dice game using *jabali's dice*, they bless you with a bit of luck, granting a +2 item bonus to your Games Lore check. You can do so frequently enough to apply this bonus while Earning Income using Games Lore, but only one user at a time can do so.

**Activate—Jabali's Gamble** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You call out the shuyookh's name and title, then roll the dice. The shuyookh appears briefly to provide for your defense. Roll `r 2d6` to determine the effect. Represented by the GM, the shuyookh chooses any effect's specifications, benefiting you according to the shuyookh's whims.

**2-5**
The shuyookh casts [[Mountain Resilience]] on you.

**6-9**
The shuyookh casts [[Grasping Earth]] but you and your allies are immune to it.

**10-11**
The shuyookh casts [[Wall of Stone]]. The edges can pass through creatures, which are shunted to the side of the wall opposite that edge.

**12**
The shuyookh casts a DC 31 [[Petrify]] spell on a creature hostile and in proximity to you. If no appealing target exists, you receive a 10-11 result instead.

**Source:** `= this.source` (`= this.source-type`)
