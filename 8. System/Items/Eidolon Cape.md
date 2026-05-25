---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though it appears to be one elegant piece, an *eidolon cape* consists of a mantle for your shoulders and a detachable cape. The cape is designed to resemble your eidolon, either with a direct likeness or with features reminiscent of your eidolon. For instance, if your eidolon is a dragon, the cape might depict a stylized dragon, or it might have a pattern of colorful scales with gold trim. An eidolon cape features the sigil you share with your eidolon prominently in its design. You gain a +2 item bonus to the skill that matches your eidolon's tradition: Arcana for arcane, Religion for divine, Occultism for occult, or Nature for primal.

When you Manifest your Eidolon, the cape transforms into the eidolon, and when the eidolon unmanifests, it turns back into the cape. If the cape is attached to the mantle, it comes free immediately, and the eidolon appears adjacent to you as normal. If not, the eidolon appears in a space adjacent to the cape. With the cape detached, the mantle is still light Bulk, and the whole cloak remains invested. If the cape is out of range (beyond 100 feet, typically) or there's not enough open space for the eidolon to manifest, your attempt to Manifest your Eidolon fails.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a summoner link spell. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a summoner.

**Source:** `= this.source` (`= this.source-type`)
