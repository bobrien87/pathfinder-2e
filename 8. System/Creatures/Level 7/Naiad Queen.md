---
type: creature
group: ["Amphibious", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Naiad Queen"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: "Water"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +9, Diplomacy +20, Medicine +15, Nature +15, Performance +20, Stealth +14, Survival +15"
abilityMods: ["+0", "+5", "+4", "+3", "+4", "+7"]
abilities_top:
  - name: "Animal Empathy"
    desc: "The naiad can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Tied to the Land"
    desc: "The queen is tied to a body of water or area with a great deal of water features. <br>  <br> A nymph queen is intrinsically tied to a specific region. As long as the queen is healthy, the environment is exceptionally resilient, allowing the nymph queen to automatically attempt to counteract any spell that would harm the environment (such as the [[Blight]] ritual), using her spell DC with a counteract rank equal to the highest-rank druid spell she can cast. <br>  <br> When the nymph queen becomes physically or psychologically unhealthy, however, her warded region eventually becomes twisted or unhealthy as well. In that case, restoring the nymph queen swiftly heals the entire region."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "26; **Fort** +15, **Ref** +18, **Will** +17"
health:
  - name: HP
    desc: "100; **Weaknesses** cold iron 10; **Resistances** fire 10"
abilities_mid:
  - name: "Nymph's Beauty"
    desc: "30 feet. A creature that fails its save is [[Stunned]] 1 and becomes stunned 1 each time it starts its turn within the aura for the next 24 hours, even if it can't see the naiad queen. <br>  <br> Creatures that start their turn in the aura must succeed at a DC 23 [[Will]] save or suffer an effect described in the nymph queen's entry."
  - name: "Water Healing"
    desc: "For every 10 minutes a naiad spends soaking in any body of water in her domain, she regains 30 Hit Points."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Aqueous Fist +18 (`pf2:1`) (agile, finesse, magical, water), **Damage** 2d8+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Water Orb +18 (`pf2:1`) (magical, water), **Damage** 4d6 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 28, attack +18<br>**4th** (2 slots) [[Heal]], [[Summon Animal]]<br>**3rd** (3 slots) [[Aqueous Orb]], [[Earthbind]], [[Heal]]<br>**2nd** (3 slots) [[Animal Messenger]], [[One with Plants]], [[Revealing Light]]<br>**1st** (3 slots) [[Air Bubble]], [[Fleet Step]], [[Gust of Wind]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Guidance]], [[Light]], [[Stabilize]]"
  - name: "Primal Innate Spells"
    desc: "DC 28, attack +20<br>**1st** [[Charm]], [[Create Water]], [[Hydraulic Push]], [[Tidal Surge]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` Nymph queens can transform between their original form, which looks much like a typical nymph of their kind, and any Small or Medium humanoid form, typically choosing a more humanoid-looking version of their natural form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Focus Beauty"
    desc: "`pf2:1` If a target already affected by nymph's beauty fails its save, the image of the queen sears into the creature's mind, effectively blinding the creature until its vision is restored with sound body or a similar effect. <br>  <br> The naiad queen can Dismiss the effect. <br>  <br> The nymph queen focuses her beauty upon a target, who must attempt a save against her nymph's beauty aura (DC 23 [[Will]] save). If the creature fails and was already affected by the aura, it takes a greater effect described in the nymph queen's entry. <br>  <br> A nymph queen can Focus Beauty on a given creature only once per turn."
  - name: "Inspiration"
    desc: "`pf2:3` The nymph queen inspires a single intelligent creature by giving that creature a token of her favor, typically a lock of her hair, though it can be some other significant object as well. As long as the creature carries her token and remains in good standing with her, the creature gains a +1 status bonus to all Crafting checks, Performance checks, and Will saves. <br>  <br> If the nymph grants her token to a bard, and she's the bard's muse, the queen chooses one additional benefit granted by her token: a +1 status bonus to all Lore checks, a +2 status bonus to Performance checks when determining the effects of compositions, a +4 status bonus to untrained skill checks, or a +2 status bonus to Will saves against fey. <br>  <br> > [!danger] Effect: Nymph Queen's Inspiration"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Naiad queens rule over pristine wildernesses centered around untouched lakes, massive rivers, or other collective bodies of fresh water. Bards' songs and artists' paintings of these powerful nymphs tend to depict naiad queens in their slightly more humanoid forms, which they don when they make the rare journey into civilized lands to garner allies, gather news, or gauge threats.

Most naiad queens treat those who respect their domains with kindness, but they're fierce—and quick to eliminate foes. Their blinding beauty and breadth of offensive spells make naiad queens fierce opponents if forced into a fight.

Nymphs are a family of fey that take the form of beautiful humanoids with elven features and have a deep association with the natural world. The most common of their kind are the dryads, which are spirits that embody great trees, but many other kinds of nymphs exist, including naiads, who watch over bodies of water. All nymphs are guardians of some element of nature, typically a specific tree or pond, or even-in the case of nymph queens-whole forests or massive bodies of water

Nymph Queens
Nymph queens are powerful nymphs who rule over entire regions of untouched wilderness, not just single trees or ponds. Every variety of nymph can have a queen. Naiad queens are among the most prominent, and more often interact with nearby mortals. Thus, some scholars refer to naiad queens as simply "nymphs."

```statblock
creature: "Naiad Queen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
