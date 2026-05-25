---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kanya"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +17, Deception +16, Diplomacy +18, Nature +14, Performance +20, Religion +14, Survival +12"
abilityMods: ["+4", "+3", "+5", "+2", "+3", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Muse's Courage"
    desc: "Any [[Courageous Anthem]] the kanya casts grants a +2 status bonus instead of +1. <br>  <br> > [!danger] Effect: Spell Effect: Courageous Anthem (Kanya)"
armorclass:
  - name: AC
    desc: "25; **Fort** +14, **Ref** +16, **Will** +16"
health:
  - name: HP
    desc: "135; **Weaknesses** cold iron 10, unholy 10"
abilities_mid:
  - name: "Free Expression"
    desc: "A kanya's auditory and sonic effects attempt to counteract any effect that would directly control, manipulate, or prevent them from expressing themself freely, such as [[Silence]]. They can also spend an action, which has concentrate trait, to speak forcefully and counteract such effects. The counteract modifier is +16 in either case."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +18 (`pf2:1`) (holy, magical, versatile p), **Damage** 1d8+10 slashing plus 1d6 sonic"
  - name: "Melee strike"
    desc: "Tail +17 (`pf2:1`) (agile, holy, magical, reach 10 ft.), **Damage** 2d6+10 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +18<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]]<br>**2nd** [[Clear Mind]], [[Invisibility]], [[Noise Blast]]<br>**1st** [[Charm]], [[Counter Performance]], [[Courageous Anthem]], [[Daze]], [[Detect Magic]], [[Figment]], [[Light]], [[Soothe]], [[Summon Instrument]], [[Uplifting Overture]]"
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Kanyas are bearers of blessings and fortune, as well as harbingers of wisdom and spiritual growth. They are generally peaceful but quick to act if a community they are residing in is threatened. They pride themselves on inspiring mortals to such joy that they express it through the arts, leading to their common moniker as "muses." More than one bard looks to a kanya as their personal inspiration, yet much like inspiration, kanyas come and go as they please. They wander the world as they will, offering rain, generosity, wisdom, and support to whomever pleases them.

Kanyas sometimes secretly follow the adventures of mortal heroes to record their stories as epic poems and songs, which they then perform in the packed mead halls of Elysium. When pursuing such goals, kanyas take pains to use their innate spells to remain in hiding, as they would rather observe and record events without "polluting" them with their own intervention. Nevertheless, a kanya who sees their charge faced with certain death often cannot resist the urge to intervene and save the day. Inevitably, this brings a close to the kanya's chronicles, as their relationship with their subject invariably shifts from one of detached observation to friendship or more. Yet, kanyas remain hesitant to involve themselves for overlong in a mortal's life, in part because they fear what sort of fiendish attention their presence might attract, but mostly out of respect for the mortal's own destiny. A kanya would, all things being equal, prefer to let mortals choose their own fate rather than run the risk of sending someone down a path to which their heart is not set.

Azatas are manifestations of freedom and unestrained joy—kindly celestials with a penchant for curious exploration, spontaneous revelry, and whimsical quests. Born of good dreams and heartfelt wishes for a better world, they reside in the untamable wilds of Elysium. Azatas are passionate and mercurial, as beautiful and bright as a child's fantasy, but also fiercely loyal to those they hold dear. They act quickly and directly against fiendish and foul influences, but they tend to avoid guiding mortal affairs otherwise, allowing people to choose their own destiny without the meddling of otherworldly forces.

Azatas reject the dual chains of both duty and tyranny, but also the heavy chains of despair that reality so often inflicts upon those who live in it. This can give them a dubious reputation with other celestials, who consider azatas to be flighty and unreliable, but azatas know that unrelenting self-sacrifice can be just as destructive to the soul as evil. Azatas refuse to compromise the beauty of the world with such banality, instead living without regret and savoring every triumph and agony they encounter upon the way.

```statblock
creature: "Kanya"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
