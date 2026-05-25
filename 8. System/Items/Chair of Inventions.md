---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 875}"
usage: "other"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wheelchair is outfitted with a variety of tools and devices to assist with the creation and production of a number of mechanical implements. While seated in a chair of inventions, you can use a Superb Repair Toolkit as though you are wearing it; it doesn't count against your Bulk limit or maximum worn items.

**Activate** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** The chair deploys a complete Expanded Alchemist's Lab. The chair is immobile while this lab is deployed, but levers and gears in the chair allow you to easily retrieve and access everything you need from both the attached superb repair toolkit and the deployed lab to Craft. This setup is highly efficient and gives you a +2 circumstance bonus to [[Earn Income]] using Crafting.

**Source:** `= this.source` (`= this.source-type`)
