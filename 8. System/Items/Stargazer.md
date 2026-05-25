---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Invested]]", "[[Magical]]", "[[Scrying]]", "[[Thrown 10]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you invest this clear quartz crystal ball, it orbits your head like an aeon stone. As long as you have the stargazer invested, you can use an Interact action to direct it to orbit one of your hands where you can telekinetically smash the orb into foes, wielding it as a *+2 greater striking returning club*. While you're directing the stargazer, your hand is full, and you can send it back to your head with another Interact action. On a critical hit, the *stargazer* pulses with hypnotic starlight, [[Dazzling]] the struck creature for 1 round. A *stargazer* doesn't add critical specialization effects.

**Source:** `= this.source` (`= this.source-type`)
