---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 600}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

This large handbell is made from cast bronze and has a wooden handle. The outside of the bell is covered in fine etchings, showing a group of varied people sitting around a table with clouds obscuring anyone in the background. The clapper is curiously absent from this bell and, when idly rung, it produces no audible sound.

**Activate—Ring in the Quiet** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** The silent bell creates an invisible wall surrounding a cube, 20 feet to a side, that prevents sound from passing into or from the cube for 10 minutes. The wall isn't solid and doesn't prevent anything but sound from passing through. Since the cube is invisible, creatures can still read lips and body language through the wall.

**Source:** `= this.source` (`= this.source-type`)
