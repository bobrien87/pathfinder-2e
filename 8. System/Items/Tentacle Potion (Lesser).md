---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 33}"
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

Upon consuming this mottled, foul-tasting liquid, the tentacle potion causes you to extrude a long, flexible limb of ectoplasm. Your clothing doesn't need to accommodate this limb of ghostly matter, which can extrude through your clothing and armor. The limb lasts 1 hour, and you can Dismiss the activation. You can't hide or disguise the tentacle. You can use the limb to perform simple Interact actions, such as opening an unlocked door. Your limb can't perform actions that require significant manual dexterity, including any action that would require a check to accomplish. You can't use it to hold items. At one time, you can have only one extra limb from any version of this potion. Stronger tentacle potions replace the effects of weaker ones.

If you have the Flexible Tail or Skillful Tail feats, the Tailed Goblin heritage, or a similar feature the GM believes would benefit, this potion can instead fortify your tail. A fortified tail benefits from any tentacle potion as if the potion were the next better type.

**Source:** `= this.source` (`= this.source-type`)
