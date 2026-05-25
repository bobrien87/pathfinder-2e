---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Force]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 100}"
usage: "affixed-to-a-thrown-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You hit a creature with the affixed weapon.

This delicate dawnsilver chain strung with tiny shuriken is wound tightly around the handle of the affixed weapon. When you Activate the chain, three *+1 striking shuriken* made from magical force materialize in the target's space and split off to attack other creatures. Attempt up to three shuriken Strikes that must each target a different creature and can't target the creature you hit to trigger this talisman. These Strikes use your attack modifier but originate from the hit creature's space. These attacks count toward your multiple attack penalty, but the penalty doesn't increase until after all three attacks have been made. The shuriken deal force damage instead of their normal type, and each shuriken vanishes after its attack.

**Source:** `= this.source` (`= this.source-type`)
