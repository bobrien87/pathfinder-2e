---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ragged cloak doesn't appear to be anything special at first glance, seemingly made from mangy black bear fur with various rings of blackened iron piercing the edge of the skin. While somewhat off-putting, the mantle grants a +2 status bonus to all Fortitude saving throws against disease and poison. When you invest the mantle, you either increase your Constitution modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** R (manipulate)

**Frequency** once per round

**Trigger** You take damage

**Effect** Drawing the cloak around you, you reduce the damage taken by 10.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** If you're currently afflicted by a poison or a disease, you can hold the cloak tight to your body and immediately attempt a saving throw to end the effect. If that saving throw succeeds, you end the effect of either the poison or disease no matter the stage of the affliction. Furthermore, you gain immunity to that poison or disease for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
