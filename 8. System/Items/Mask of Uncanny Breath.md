---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Occult]]"]
price: "{'gp': 1200}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A thin wooden mask carved in the shape of a skull, monstrous face, or eerily featureless visage, a *mask of uncanny breath* fully covers your face. While wearing it, each breath you take feels cool and pure, perfectly flowing to feed your qi. You gain resistance 10 to inhaled poisons and can breathe in an airless or toxic environment. When you breathe in, fragments of bizarre knowledge flow through you, granting you a +2 item bonus to Occultism checks.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast an occult monk qi spell. If not used by the end of your turn, this Focus Point is lost.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** Your unarmed Strike damages a creature that breathes

**Effect** The mask contorts and inhales, sucking breath from your target's lungs. The target falls [[Unconscious]] but doesn't fall [[Prone]] or drop what it's holding. It wakes up at the end of your turn if it hasn't been woken up already.

**Craft Requirements** You are a monk with occult qi spells.

**Source:** `= this.source` (`= this.source-type`)
