---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Aura]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
price: "{'gp': 100}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The faceplate of a dread helm has a fierce visage that magnifies the effects of fear. Concealed within is a reservoir that can hold a single Dread Ampoule, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** A dread ampoule is installed in the helm

**Effect** The dread ampoule atomizes, creating a fear-inducing mist that hangs around your face for 3 rounds. The mist grants an item bonus to Intimidation checks equal to the dread ampoule's item bonus. The mist also deals mental damage equal to the dread ampoule's splash damage to all creatures within a @Template[type:emanation|distance:5] other than you. The activation uses up the dread ampoule, and the helm can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
