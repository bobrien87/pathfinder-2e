---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of soft and subtle black leather, these gloves fit tightly but aren't uncomfortable and don't impede your sense of touch. As long as you're trained in Thievery while wearing these gloves, you're always considered one skill rank higher than your actual rank. If you possess a Legendary skill rank in Thievery, you gain a +2 item bonus to Thievery checks instead. When you invest the gloves, you either increase your Dexterity modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You fail or critically fail a Thievery skill check

**Effect** If you failed the Thievery skill check, you succeed at that check instead. If you critically failed, you fail instead.

**Source:** `= this.source` (`= this.source-type`)
