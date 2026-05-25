---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 1600}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Prerequisites** You have the affixed shield raised.

**Trigger** You would take damage of a type depending on the talisman's dragon type.

This decorative shield emblem contains the gilded claw of a dragon mounted in a setting of high-grade adamantine alloy. It protects against a damage type depending on the type of dragon the claw came from (see the sidebar). When you Activate the scutcheon, you and all of your carried, wielded, or worn items gain immunity to all damage of that type until the end of your next turn.

If you have a dragonclaw scutcheon, dragonscale cameo, and dragontooth trophy attached to your items, and they all correspond to the same type of dragon, you gain an extra benefit. When you Activate any of these talismans, you gain the ability to cast an 8th-rank [[Dragon Breath]] focus spell (DC 35 [[Reflex]] save) as an innate spell once before the end of your next turn. Use the dragon type that matches the talismans; you can Cast the Spell this way without spending a Focus Point. Because each talisman disintegrates when used, you can't get this benefit again until you've attached a replacement.

**Craft Requirements** Supply one claw from an adult or older dragon.

**Source:** `= this.source` (`= this.source-type`)
