---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tikbalang"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +20, Deception +21, Nature +14, Stealth +17, Survival +16"
abilityMods: ["+5", "+4", "+4", "-1", "+3", "+6"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "197; **Weaknesses** mental 10"
abilities_mid:
  - name: "Believe the Lie"
    desc: "The tikbalang takes a –2 circumstance penalty to saves against illusion spells and to their Will DC against checks to Lie to them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile), **Damage** 2d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Hoof +20 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+8 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29, attack +21<br>**8th** [[Quandary (once per week)]]<br>**4th** [[Mirage]]<br>**3rd** [[Hypnotize]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The tikbalang takes on the appearance of any Medium or Large humanoid. This doesn't change the tikbalang's Speed or their attack and damage modifiers with their Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Flailing Thrash"
    desc: "`pf2:2` The tikbalang makes two fist Strikes, with each Strike dealing an extra 1d6 untyped damage against creatures grabbing or [[Grabbed]] or [[Restrained]] by the tikbalang. The multiple attack penalty doesn't increase until after both attacks."
  - name: "Unnatural Leap"
    desc: "`pf2:1` The tikbalang jumps up to their Speed horizontally, or half that vertically."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Tikbalangs are forest creatures that delight in leading travelers astray. They deceive and mislead with their formidable magic, leaping from tree to tree while laughing or neighing uncontrollably. While not malicious, neither are they empathetic to the plight of their victims. Tikbalangs would sooner forget about those whom they've tricked and leave these unfortunate souls to die than lead them back to their intended path through guilty altruism.

Tikbalangs' occult magic stems from the esoteric mystery of believing a lie. In the moment of crafting illusions or conjuring extradimensional spaces, tikbalangs themselves believe that what they're creating is real. This conviction makes their spells harder to resist, and this same principle also makes them very effective liars. But this readiness to believe also makes them susceptible to deceptions and illusions in turn, and they're particularly vulnerable to mind games. Lone travelers without magic of their own are advised to learn riddles, sleight of hand, or other tricks to defend against tikbalangs' oft-deadly entertainment. Other whispers suggest wearing one's shirt inside out to confuse the creatures, or passing by a tikbalang's forest quietly to avoid drawing their attention.

Unlike some illusionists, tikbalangs can also rely on their physical prowess should the need arise. They have unusually long legs that end in cloven hooves and stand as tall as ogres when upright. Skilled climbers and leapers, they're also well known as master wrestlers, where their long limbs put them at a distinct advantage over their foes. They have elongated faces that, when combined with their well-kept hair, suggest an equine appearance—although some tikbalangs have saurian or birdlike faces instead.

```statblock
creature: "Tikbalang"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
