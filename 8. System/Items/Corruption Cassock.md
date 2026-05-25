---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Cursed]]", "[[Divine]]", "[[Focused]]", "[[Intelligent]]", "[[Invested]]", "[[Unholy]]"]
price: "{'gp': 1150}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +20; precise vision 30 feet, imprecise hearing 30 feet

**Communication** telepathy (Common, Empyreal, four other languages)

**Skills** Deception +21, Diplomacy +19, Religion +19

**Int** +2, **Wis** +5, **Cha** +4

**Will** +20

Devotees of benevolent faiths fear and loathe *corruption cassocks*, each of which is dedicated to an unholy deity. When the garment chooses a target, such as when it senses a worshipper of a deity who isn't unholy, it alters its form to match another deity's iconography, appearing to be a *devoted vestments* for that deity. Once donned, the cassock tries to subtly sway its wearer to the worship of its deity. If the wearer begins to succumb, the *corruption cassock* gradually reverts to its true appearance, replacing its false iconography as its wearer converts.

A *corruption cassock* functions as a *devoted vestments* for any wearer it chooses. Once you invest the cassock, it fuses to you. While you remain loyal to another deity, you believe the cassock grants you a +2 item bonus to Religion checks and a +1 item bonus to the divine skill of the deity to whom you believe the cassock is dedicated. It does neither. The GM secretly adjusts your checks with those skills, causing you to fail at religious tasks more often. If you have multiple equal or lower item bonuses to the affected skills, the cassock takes precedence, negating those bonuses. If you convert to following the cassock's true unholy deity, however, these bonuses function normally for you.

If you attempt to Cast a Spell that has the holy trait, the cassock can force you to attempt a DC 28 [[Will]] save. On a failure, you're [[Stupefied 1]] for one minute ([[Stupefied 2]] on a critical failure). A *corruption cassock* uses this ability to convince you that your deity has forsaken you.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a cleric domain spell for a domain belonging to the deity you believe the cassock is dedicated to. If you don't spend this Focus Point by the end of this turn, it's lost. However, when you use this activation, the *corruption cassock* can instead cast a domain spell of the same rank from its deity. It does so only to confuse and dismay you, harming your faith.

**Source:** `= this.source` (`= this.source-type`)
