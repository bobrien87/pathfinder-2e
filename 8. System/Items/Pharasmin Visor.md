---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Popular in Ustalav and other lands where undead are numerous, a *Pharasmin visor* is a valuable part of any fashionable noble's armory when attending events in places like Caliphas. This item consists of a metal skullcap helm with a pair of blue crystal lenses extending from each side on metal armatures that can be moved independently in front of or away from the eyes. The helm can appear as either gleaming silver or dull black, and the wearer can alter its appearance whenever they invest the visor.

**Activate—Pharasma's Disdain** `pf2:2` (manipulate, mental)

**Frequency** once per day

**Effect** You adjust the visors so that both are lowered. Your vision becomes obscured, causing you to become [[Dazzled]]. At the same time, a tiny fraction of Pharasma's notice seeps out of the visor to fill the area around you in a @Template[type:emanation|distance:30]. All undead creatures in this area take 12d6 spirit damage (DC 30 [[Will]] save). At the end of your turn, both visors automatically rise back up, but you remain dazzled until the start of your next turn.

**Activate—Pierce the Night** `pf2:1` (manipulate)

**Effect** You adjust the helm so that only the left visor is lowered. You gain darkvision until you adjust the visors again or until the item is no longer invested by you, whichever comes first.

**Activate—Reveal the Unseen** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You adjust the helm so that only the right visor is lowered. You can see [[Invisible]] creatures as though they weren't invisible, although their features are blurred, making them [[Concealed]] and difficult to identify. You can also see incorporeal creatures like ghosts when they have phased through an object if you are within 10 feet of an object's surface; they look like blurry shapes seen through those objects. This effect lasts until 8 hours pass, until you adjust the visors again, or until the item is no longer invested by you, whichever comes first.

**Activate—See Through Death** `pf2:1` (manipulate)

You adjust the visors so that both are raised. The *Pharasmin visor* grants a +2 item bonus on all saving throws against effects with the death trait.

**Source:** `= this.source` (`= this.source-type`)
