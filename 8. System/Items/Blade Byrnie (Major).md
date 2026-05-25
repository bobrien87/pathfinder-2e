---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Flexible]]", "[[Noisy]]"]
price: "{'gp': 35000}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Instead of chain links, this *+3 greater resilient chain shirt* is assembled from metal "leaves" that each resemble a small blade.

**Activate** `pf2:1` (manipulate)

**Effect** You pull a link from the armor, which transforms into a *+3 greater striking [[Dagger]]*. The dagger disappears and reappears as a link in the armor after you Strike with it, or at the end of this turn if you don't make a Strike. You can Activate the blade byrnie in place of an Interact action to draw a weapon for abilities such as the [[Quick Draw]] feat.

Upgrading the runes on the blade byrnie makes the daggers pulled from it more powerful. The daggers have a *+2 weapon potency* rune if the armor has a *+2 armor potency* rune, or a *+3 weapon potency* rune if the armor has a *+3 armor potency* rune.

**Source:** `= this.source` (`= this.source-type`)
