---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'gp': 9000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This pale shaft of wood has skulls and the mournful faces of the dead carved into its surface. Cold to the touch, it brings a slight chill to the air and smells of freshly disturbed earth.

**Activate—Gather the Fallen** `pf2:3` (manipulate, occult, void)

**Frequency** once per day

**Effect** You plant the baton into the ground, the soil softly parting to allow it to be solidly seated. Doing so summons a cloud of ghostly spirits in a @Template[type:burst|distance:30]. All creatures within the cloud become [[Concealed]], and all creatures outside the cloud become concealed to creatures within it. The spirits deal @Damage[8d6[void]|options:area-damage|traits:manipulate,occult,void] damage to each creature who enters or begins their turn in the cloud ([[Fortitude]] save). You are unaffected by the cloud. This effect lasts 1 minute or ends if an adjacent creature spends an Interact action to knock the baton over.

**Source:** `= this.source` (`= this.source-type`)
