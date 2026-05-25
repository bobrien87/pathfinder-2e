---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *instinct crown* is a magical headpiece imbued with the essence of instincts that barbarians draw upon in combat. Each crown is fashioned to represent the instinct it's tied to, such as a wolf's head for an animal instinct crown or a simple helmet with Jotun runes for a *giant instinct crown*. When worn, the crown allows you to tap further into your instincts, granting you even greater benefits if the crown's essence matches your instinct. You must be able to [[Rage]] to use the crown's activations.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You roll initiative

**Requirements** You have [[Quick Tempered]] and meet its requirements

**Effect** You use Quick-Tempered and gain 10 additional temporary Hit Points from your Rage.

**Activate** `pf2:1` (concentrate, rage)

**Frequency** once per day

**Requirements** You're raging, and the crown's instinct matches your barbarian instinct

**Effect** Your boundless fury allows you push past your natural limits, moving with unmatched speed. You become [[Quickened]] until the end of your rage. You can use your extra action only to Stride or Strike.

> [!danger] Effect: Instinct Crown

**Source:** `= this.source` (`= this.source-type`)
