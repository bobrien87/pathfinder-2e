---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 140}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You fail or critically fail a Deception, Diplomacy, or Intimidation check to [[Coerce]], [[Lie]], [[Make an Impression]], or [[Request]]

**Requirements** You're a master in the skill you failed with.

This ornate locket, usually containing a faceless, humanoid portrait, is typically worn on a chain around the neck or attached to your clothing. When activated, the charm casts a [[Rewrite Memory]] spell (DC 26 [[Will]] save) against a single target of the check, removing all memory of your failed attempt and potentially allowing you to make another attempt. The effect can't remove more than 3 minutes of memories from its target.

**Source:** `= this.source` (`= this.source-type`)
