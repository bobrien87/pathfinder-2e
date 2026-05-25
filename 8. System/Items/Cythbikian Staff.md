---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Fungus]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 5800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *Cythbikian staff* is a gnarled length of rotting wood, riddled with mold and fungal growths. Originally called the Zibikian staff in honor of its creator, the green man Zibik, with whom Ghorus communed before magically receiving this staff. Ghorus spent years using samples of the staff's spores to invent weapons for his war against Taldor.

When you invest this staff, a thin layer of fungi grows on your hands, remaining until your next daily preparations. If an enemy takes damage from any of the spells you cast by the *Cythbikian staff*, this fungus spreads up your arms, and you gain temporary Hit Points equal to double that spell's level. These temporary Hit Points last 10 minutes.

**Activate—Rule by Roots** `pf2:3` (fungus, manipulate)

**Frequency** once per week

**Effect** You plunge the *Cythbikian staff* into the earth, causing a vast fungal network to spread out from the staff, coating the ground, plants, structures, and all creatures in a @Template[emanation|distance:100] ([[Reflex]] save avoids) until the staff is removed or 24 hours have passed. Non-magical plants in the area die. A creature covered by these fungal growths is [[Grabbed]] and controlled, physically, by the fungus, as it moves them around like a living puppet. At the beginning of a grabbed creature's turn, they can attempt to `act escape show-dc=all dc=34`. On a failure, the fungus forces them to spend all of their remaining actions moving toward and attacking the nearest creature in the area using melee Strikes with any weapon at their disposal. The fungal growths pay no mind to how the bodies under their control operate, and grabbed creatures are twisted, bent, and contorted in ways that harm their body. Each round, at the end of a grabbed creature's turn, they take 8d6 bludgeoning damage from this painful manipulation ([[Fortitude]] save). A creature that successfully Escapes or is physically removed from the area is no longer grabbed or controlled. When the *Cythbikian staff* is removed from the ground, or after 24 hours have passed, the mold dies and this effect ends. Over the course of a week, the mold decays and fertilizes the soil, providing valuable nutrients to the soil and preparing the region for new plant growth.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Timber]]

- **1st** [[Wall of Shrubs]], [[Wooden Fists]]

- **2nd** [[Oaken Resilience]], [[Splinter Volley]]

- **3rd** [[Sudden Blight]], [[Wall of Thorns]]

- **4th** [[Murderous Vine]], [[Fungal Infestation]]

- **5th** [[Life Draining Roots]], [[Plant Form]]

- **6th** [[Lignify]], [[Tangling Creepers]]

**Source:** `= this.source` (`= this.source-type`)
