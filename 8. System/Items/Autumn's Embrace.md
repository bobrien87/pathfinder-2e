---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Laminar]]"]
price: "{'gp': 2000}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Woven by fey seamstresses as rewards for servants of nature, countless leaves continually changing colors in autumnal hues comprise *autumn's embrace*, a suit of *+2 invisibility resilient leaf weave*. Leaves shed from the armor as they might fall in autumn. When activating the armor's [[Invisibility]] property rune, you disappear in a swirl of colorful leaves.

**Activate** `pf2:2` (aura, concentrate)

**Frequency** once per day

**Effect** You call forth a storm of leaves from *autumn's embrace*. These leaves swirl in a @Template[emanation|distance:20] for 1 minute. Creatures within the area are [[Concealed]], and creatures outside the area are concealed to creatures within the leaves. However, you can see through this concealment. You can Dismiss the activation.

**Source:** `= this.source` (`= this.source-type`)
