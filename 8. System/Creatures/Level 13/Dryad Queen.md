---
type: creature
group: ["Fey", "Nymph"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dryad Queen"
level: "13"
rare_01: "Uncommon"
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
    desc: "+25; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Muan"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +19, Crafting +23, Deception +30, Diplomacy +30, Intimidation +27, Nature +24, Performance +28, Stealth +25, Survival +24"
abilityMods: ["+2", "+6", "+6", "+4", "+4", "+8"]
abilities_top:
  - name: "Nature Empathy"
    desc: "The dryad can ask questions of, receive answers from, and use the Diplomacy skill with animals and plants."
  - name: "Tied to the Land"
    desc: "The dryad queen is tied to a forest or other woodland. <br>  <br> A nymph queen is intrinsically tied to a specific region. As long as the queen is healthy, the environment is exceptionally resilient, allowing the nymph queen to automatically attempt to counteract any spell that would harm the environment (such as the [[Blight]] ritual), using her spell DC with a counteract rank equal to the highest-rank druid spell she can cast. <br>  <br> When the nymph queen becomes physically or psychologically unhealthy, however, her warded region eventually becomes twisted or unhealthy as well. In that case, restoring the nymph queen swiftly heals the entire region."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "35; **Fort** +24, **Ref** +26, **Will** +24"
health:
  - name: HP
    desc: "220; **Weaknesses** cold iron 10, fire 10"
abilities_mid:
  - name: "Nymph's Beauty"
    desc: "30 feet. On a failed save, the target is [[Immobilized]] in awe for 1 minute. <br>  <br> Creatures that start their turn in the aura must succeed at a DC 30 [[Will]] save or suffer an effect described in the nymph queen's entry."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Branch +27 (`pf2:1`) (finesse, magical), **Damage** 3d12+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Leaves +27 (`pf2:1`) (plant, primal, range 60 ft.), **Damage** 3d8+6 slashing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 35, attack +25<br>**7th** (2 slots) [[Regenerate]], [[Summon Plant or Fungus]]<br>**6th** (3 slots) [[Chain Lightning]], [[Cursed Metamorphosis]], [[Tangling Creepers]]<br>**5th** (3 slots) [[Banishment]], [[Heal]], [[Howling Blizzard]]<br>**4th** (3 slots) [[Fly]], [[Mountain Resilience]], [[Resist Energy]]<br>**3rd** (3 slots) [[Earthbind]], [[Haste]], [[Wall of Thorns]]<br>**2nd** (3 slots) [[Animal Messenger]], [[Clear Mind]], [[Revealing Light]]<br>**1st** (3 slots) [[Fleet Step]], [[Gust of Wind]], [[Pest Form]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Guidance]], [[Light]], [[Stabilize]]"
  - name: "Primal Innate Spells"
    desc: "DC 35, attack +25<br>**8th** [[Impaling Briars]]<br>**5th** [[Nature's Pathway]]<br>**4th** [[Suggestion]]<br>**2nd** [[Entangling Flora]], [[One with Plants]], [[Shape Wood]]<br>**1st** [[Charm]], [[Tangle Vine]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` Nymph queens can transform between their original form, which looks much like a typical nymph of their kind, and any Small or Medium humanoid form, typically choosing a more humanoid-looking version of their natural form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Focus Beauty"
    desc: "`pf2:1` On a failed save, if the target was already affected by the dryad queen's beauty, the target can't use hostile actions against the dryad queen for 1 hour. <br>  <br> The nymph queen focuses her beauty upon a target, who must attempt a save against her nymph's beauty aura (DC 30 [[Will]] save). If the creature fails and was already affected by the aura, it takes a greater effect described in the nymph queen's entry. <br>  <br> A nymph queen can Focus Beauty on a given creature only once per turn."
  - name: "Inspiration"
    desc: "`pf2:3` The nymph queen inspires a single intelligent creature by giving that creature a token of her favor, typically a lock of her hair, though it can be some other significant object as well. As long as the creature carries her token and remains in good standing with her, the creature gains a +1 status bonus to all Crafting checks, Performance checks, and Will saves. <br>  <br> If the nymph grants her token to a bard, and she's the bard's muse, the queen chooses one additional benefit granted by her token: a +1 status bonus to all Lore checks, a +2 status bonus to Performance checks when determining the effects of compositions, a +4 status bonus to untrained skill checks, or a +2 status bonus to Will saves against fey. <br>  <br> > [!danger] Effect: Nymph Queen's Inspiration"
  - name: "Tree Meld"
    desc: "`pf2:2` A [[One with Plants]] spell cast by a dryad has an unlimited duration. <br>  <br> In addition, if the dryad merges with any tree in her domain, she can choose to instead enter an extradimensional living space within the tree, and can bring up to eight adjacent, willing creatures with her; the spell gains the extradimensional trait. The dryad can still be expelled from this space."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Also called a hamadryad, a dryad queen rules over an entire forest, or a portion of an incredibly large forest, leading and protecting all dryads within. Dryad queens often have strange relationships with powerful and deadly fey, working together in a dualistic way despite their differences, with the queen representing nature's wonders and the other fey representing nature's wrath.

Nymphs are a family of fey that take the form of beautiful humanoids with elven features and have a deep association with the natural world. The most common of their kind are the dryads, which are spirits that embody great trees, but many other kinds of nymphs exist, including naiads, who watch over bodies of water. All nymphs are guardians of some element of nature, typically a specific tree or pond, or even-in the case of nymph queens-whole forests or massive bodies of water

Nymph Queens
Nymph queens are powerful nymphs who rule over entire regions of untouched wilderness, not just single trees or ponds. Every variety of nymph can have a queen. Naiad queens are among the most prominent, and more often interact with nearby mortals. Thus, some scholars refer to naiad queens as simply "nymphs."

```statblock
creature: "Dryad Queen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
