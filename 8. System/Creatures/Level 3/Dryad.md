---
type: creature
group: ["Fey", "Nymph"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dryad"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: "Nymph"
trait_03: "Plant"
trait_04: "Wood"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Muan"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +5, Crafting +7, Diplomacy +9, Nature +13, Stealth +9, Survival +12"
abilityMods: ["+0", "+4", "+1", "+2", "+3", "+4"]
abilities_top:
  - name: "Nature Empathy"
    desc: "The dryad can ask questions of, receive answers from, and use the Diplomacy skill with animals and plants."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "55; **Weaknesses** cold iron 5, fire 5"
abilities_mid:
  - name: "Tree Dependent"
    desc: "A naiad is bonded to a great tree. If she is more than 300 feet away from it for 24 hours or more, she gains the weak adjustments until she returns. She can perform a 24-hour ritual to bond herself to a new great tree."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Branch +12 (`pf2:1`) (finesse, magical), **Damage** 1d12+2 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20, attack +12<br>**5th** [[Nature's Pathway]]<br>**4th** [[Suggestion]]<br>**2nd** [[Entangling Flora]] (At Will), [[One with Plants (At Will, See Tree Meld)]]<br>**1st** [[Charm]], [[Tangle Vine]]"
abilities_bot:
  - name: "Tree Meld"
    desc: "`pf2:2` A [[One with Plants]] spell cast by a dryad has an unlimited duration. <br>  <br> In addition, if the dryad merges with her bonded tree, she can choose to instead enter an extradimensional living space within the tree, and can bring up to two adjacent, willing creatures with her; the spell gains the extradimensional trait. The dryad can still be expelled from this space."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dryads are fey guardians of the trees and creatures who dwell in wooded areas. They prefer using indirect methods to dissuade those who would harm their sacred groves and beloved forests, but they are not above using enchantments to enlist the aid of allies when evil threats cannot be dissuaded with words alone. In times of peace, dryads happily live secluded lives inside their trees, and a community at harmony with nature might not even realize a dryad lives nearby.

Though they watch over all the woods around them, dryads are inextricably tied to a specific tree, usually an oak. Dryads who are bonded to another type of tree are fundamentally the same, but they may differ in temperament and appearance to match their ward. For instance, kraneiai, or cherry-tree dryads, have beautiful pink coloration and concern themselves with the fragile beauty of life.

Nymphs are a family of fey that take the form of beautiful humanoids with elven features and have a deep association with the natural world. The most common of their kind are the dryads, which are spirits that embody great trees, but many other kinds of nymphs exist, including naiads, who watch over bodies of water. All nymphs are guardians of some element of nature, typically a specific tree or pond, or even-in the case of nymph queens-whole forests or massive bodies of water

```statblock
creature: "Dryad"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
