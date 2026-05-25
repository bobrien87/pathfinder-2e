---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Earth]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *robe of stone*, decorated with patterns reminiscent of gems and geodes, constantly sheds tiny amounts of dust. While wearing it, you gain imprecise tremorsense in a radius of 10 feet, and you can speak and read Petran. Also, you can eat earth (soil, sand), gems (crystals, glass), and metal instead of food to meet your daily nutrition requirements. You find eating these materials as pleasant as food—the more valuable, the more delicious.

**Activate—Become Stone** `pf2:2` (concentrate, manipulate, polymorph)

**Frequency** once per day

**Effect** The cloak casts [[Elemental Form]] on you, transforming you into an earth elemental. In addition to the spell's normal effects, you can Burrow through any earthen matter, including rock, moving at the spell's burrow Speed, leaving no tunnels or signs of your passing. Also, the range of the tremorsense you gain from the robe increases to 30 feet.

**Source:** `= this.source` (`= this.source-type`)
