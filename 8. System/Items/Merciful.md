---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Mental]]"]
price: "{'gp': 70}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Merciful weapons are sheathed in an unmistakable wispy green aura recognized by both gladiators and guards around the world. A *merciful* weapon has the nonlethal trait and can't be used to make a lethal attack. Any persistent damage the weapon would deal is negated.

On a critical hit, a *merciful* weapon causes the target to become [[Fascinated]] with the weapon's wielder for 1 minute, as the target is bombarded with feelings of guilt and remorse. This is a mental effect. If you have access to the weapon's critical specialization effect, you choose whether to use it or the *merciful* effect.

**Source:** `= this.source` (`= this.source-type`)
