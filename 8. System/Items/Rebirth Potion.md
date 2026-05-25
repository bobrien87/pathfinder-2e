---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A small bit from a humanoid—such as a hair, scale, or feather—steeps in the clear liquid of a rebirth potion. When the potion is created, this bit determines the ancestry and heritage the potion changes the imbiber to. After you drink the potion, you transform into that ancestry over 8 hours during your next period of rest, finishing the transformation after the 8 hours are up. Throughout this time, you are [[Clumsy]] 2, [[Enfeebled]] 2, and [[Stupefied 2]]. Once the transformation is complete, the potion's magic ends and can't be counteracted. Replace your ancestry Hit Points, size, Speeds, attribute boosts, attribute flaws, traits, and special abilities with those of your new ancestry. You lose your ancestry feats, selecting replacements valid for your new ancestry. You have mild control over the change, but you end up with a unique appearance fitting for your new ancestry, and some quirks of your body remain, such as relative age, general health, scars, and missing digits, limbs, or organs.

Drinking a rebirth potion of your current ancestry works normally, allowing you to rearrange some of the cited ancestry elements and change your appearance (provided you abide by the potion's limitations regarding health and age).

**Source:** `= this.source` (`= this.source-type`)
