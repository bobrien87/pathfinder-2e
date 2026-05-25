---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Laminar]]"]
price: "{'gp': 22750}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The first suit of *+3 greater resilient antimagic sankeit* made in this fashion was crafted for the Varki linnorm king Nankou, after he claimed his title by slaying a taiga linnorm. By Varki tradition, the armor was crafted using some of the slain linnorm's body to decorate the breastplate and helm, which imbued the armor with several of the linnorm's natural abilities. Though the helm is shaped like the beast's head, a linnorm's actual head would be too large for a proper helmet.

**Activate** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You breathe a @Template[cone|distance:60] of electrified vapor, dealing @Damage[17d6[electricity]|options:area-damage] to creatures in the area (DC 38 [[Reflex]] save). The electrified mist persists in the area for 2 rounds, dealing @Damage[5d6[electricity]|options:area-damage] (DC 38 basic Reflex save) to each creature that ends its turn in the mist. If you slew the linnorm this armor is made from, you can use the higher of your [[Reflex]] save{class DC or spell DC} instead of the listed DCs for this effect.

**Activate** `pf2:r` (manipulate)

**Trigger** A creature adjacent to you targets you with a melee attack

**Effect** The creature takes 4d6 piercing as previously invisible magical spines leap outwards from the armor to punish them for the attack.

**Craft Requirements** The initial raw materials must include the hide and skull of a taiga linnorm.

**Source:** `= this.source` (`= this.source-type`)
