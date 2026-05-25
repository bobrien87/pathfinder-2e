---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1800}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tanglebriar is not the only realm plagued by fiendish fungi. The soldiers of Nirmathas have long fought against a similar blight deep in Fangwood, and these boots are one of the more potent tools they've developed to help in this pursuit. Now that the Fangwood blight has been mostly contained, many of these boots have been gifted to elven soldiers, for they are equally useful to those who operate within Tanglebriar's borders. They are also regarded as great trophies for the demons and cultists who dwell within Tanglebriar, for not only can they make use of these boots' powers, but wearing something created by your enemy gives Treerazer's agents yet another way to engage in psychological warfare—they often adorn their boots with severed elf ears, or worse!

These leather boots remain covered in mud no matter how often they are cleaned. The oiled leather resists water and keeps the feet and legs dry even when wading through water, but the boots retain a damp, fungal smell reminiscent of rotting vegetation. While wearing the boots, you gain a +2 item bonus to Athletics checks to Climb or Swim and to Acrobatics checks to [[Balance]].

**Activate—Swift Sidestep** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You are about to make a Reflex saving throw against an environmental hazard or terrain feature

**Effect** The boots help you to avoid the hazard or effect, granting you a +2 status bonus to your saving throw. If you succeed at the saving throw, you become [[Quickened]] for 1 minute, but can use the additional action only to Stride.

**Activate—Fungal Stride** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You ignore the effects of difficult terrain and gain resistance 10 to damage caused by hazardous terrain. This activation lasts for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
