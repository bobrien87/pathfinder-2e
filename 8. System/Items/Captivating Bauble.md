---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Auditory]]", "[[Consumable]]", "[[Emotion]]", "[[Linguistic]]", "[[Magical]]", "[[Talisman]]", "[[Visual]]"]
price: "{'gp': 350}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (concentrate, manipulate)

**Requirements** You are a master in Deception or Diplomacy.

This talisman appears as an ornate piece of jewelry of the highest quality. When you Activate it, your speech and mannerisms become supernaturally compelling for up to 1 hour. By engaging an intelligent creature in conversation for at least 1 minute, you can cause them to become [[Fascinated]] unless they succeed at a DC 30 [[Will]] save. This fascination lasts for as long as you continue conversing or until you move at least 20 feet away. When the effect ends, the target becomes temporarily immune for 24 hours. If you or any ally within 120 feet takes an overtly hostile action while a creature is fascinated by the bauble, the bauble burns out in a shower of sparks and all its effects end.

**Source:** `= this.source` (`= this.source-type`)
