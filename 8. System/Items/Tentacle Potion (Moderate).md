---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 155}"
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

Upon consuming this mottled, foul-tasting liquid, the tentacle potion causes you to extrude a long, flexible limb of ectoplasm. Your clothing doesn't need to accommodate this limb of ghostly matter, which can extrude through your clothing and armor. The limb lasts 8 hours, and you can Dismiss the activation. You can't hide or disguise the tentacle. You can use the limb to perform simple Interact actions, such as opening an unlocked door. Your limb can't perform actions that require significant manual dexterity, including any action that would require a check to accomplish. At one time, you can have only one extra limb from any version of this potion. Stronger tentacle potions replace the effects of weaker ones.

You can use the limb to hold an item of up to light Bulk. You can also use the whole limb to hold onto a suitable anchor point, such as a tree branch, balcony, or rocky outcropping, subject to the GM's discretion. While using your limb this way, you have free use of all your other limbs, so you can perform tasks that require both hands.

If you have the Flexible Tail or Skillful Tail feats, the Tailed Goblin heritage, or a similar feature the GM believes would benefit, this potion can instead fortify your tail. A fortified tail benefits from any tentacle potion as if the potion were the next better type.

**Source:** `= this.source` (`= this.source-type`)
