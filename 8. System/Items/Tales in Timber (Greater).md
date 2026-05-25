---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]", "[[Wood]]"]
price: "{'gp': 2800}"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dozens of pictorial stories—told in wood carvings, painting, or pyrography—adorn every outer surface of this *+2 resilient wooden breastplate*. All are old, and many truly ancient, depicting tales set eons ago on the Plane of Wood. You gain a +2 item bonus to Nature checks to Recall Knowledge. If you know the [[Collective Memories]] ritual, you can use Nature instead of Occultism if you're the primary caster.

**Activate—Statue Disguise** `pf2:2`

**Frequency** once per day

**Effect** The armor makes you look like a wooden statue version of one of the creatures depicted on the armor for 1 hour. This is a 3rd-rank [[Illusory Disguise]], but it can make you look like any creature depicted on the armor. This doesn't change your size or the capabilities of your body, and it scales the appearance of the creature to match yours. You can Dismiss the activation. This disguise is just real enough to make you somewhat closer to a creature of wood. You're affected by two spells while it lasts: 4th-rank [[Oaken Resilience]] and [[Speak with Plants]]. If you stand still, you gain a +2 item bonus to Deception checks and DCs to appear as an inanimate wooden statue, in addition to the status bonus to Deception from *illusory disguise*.

**Source:** `= this.source` (`= this.source-type`)
